from django.shortcuts import render, redirect
from .forms import PersonalInfoForm
from .models import PersonalInfo

def create_resume(request):
    if request.method == 'POST':
        form = PersonalInfoForm(request.POST)
        if form.is_valid():
            personal_info = form.save(commit=False)
            personal_info.save()

            # Retrieve the job experience, skills, and education fields from the form data
            job_experience = request.POST.get('job_experience')
            skills = request.POST.getlist('skills')  # Use getlist() to retrieve multiple skills
            education = request.POST.get('education')

            # Save the job experience, skills, and education fields to the personal_info object
            personal_info.job_experience = job_experience
            personal_info.skills = '\n'.join(skills)  # Join the skills into a single string with line breaks
            personal_info.education = education
            personal_info.save()

            return redirect('resume_preview', personal_info_id=personal_info.pk)
    else:
        form = PersonalInfoForm()
    return render(request, 'resume_app/create_resume.html', {'form': form})






def resume_preview(request, personal_info_id):
    personal_info = PersonalInfo.objects.get(id=personal_info_id)

    job_experience = personal_info.job_experience.split('\n') if personal_info.job_experience else []
    skills = personal_info.skills.split('\n') if personal_info.skills else []
    education = personal_info.education.split('\n') if personal_info.education else []

    context = {
        'personal_info': personal_info,
        'job_experience': job_experience,
        'skills': skills,
        'education': education,
    }
    return render(request, 'resume_app/resume_preview.html', context)






