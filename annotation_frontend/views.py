from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from annotation_backend.models import AnnotationProject, AnnotationImage, Annotation
import json

# Home page to display all projects
def index(request):
    projects = AnnotationProject.objects.all()
    selected_project = None
    images = []

    if 'project' in request.GET and request.GET['project']:
        selected_project = get_object_or_404(AnnotationProject, id=request.GET['project'])
        images = AnnotationImage.objects.filter(project=selected_project)

    return render(request, 'index.html', {
        'projects': projects,
        'selected_project': selected_project,
        'images': images
    })

# Save Annotations for an Image
def save_annotations(request, image_id):
    if request.method == 'POST':
        image = get_object_or_404(AnnotationImage, id=image_id)
        data = json.loads(request.body)
        
        # Save one annotation
        Annotation.objects.create(
            image=image,
            image_label=data.get('label', 'No Label'),
            x=float(data.get('x', 0)),
            y=float(data.get('y', 0)),
            width=float(data.get('width', 0)),
            height=float(data.get('height', 0))
        )
        return JsonResponse({'status': 'success', 'message': 'Annotation added successfully to the database !'})
    return JsonResponse({'status': 'failed', 'message': 'Invalid request'}, status=400)
