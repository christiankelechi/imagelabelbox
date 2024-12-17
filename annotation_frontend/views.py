from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from annotation_backend.models import AnnotationProject, AnnotationImage, Annotation
import json

# # Home page to display all projects
# def index(request):
#     projects = AnnotationProject.objects.all()
#     selected_project = None
#     images = []

#     if 'project' in request.GET and request.GET['project']:
#         selected_project = get_object_or_404(AnnotationProject, id=request.GET['project'])
#         images = AnnotationImage.objects.filter(project=selected_project)

#     return render(request, 'index.html', {
#         'projects': projects,
#         'selected_project': selected_project,
#         'images': images
#     })

# # Save Annotations for an Image
# def save_annotations(request, image_id):
#     if request.method == 'POST':
#         image = get_object_or_404(AnnotationImage, id=image_id)
#         data = json.loads(request.body)
        
#         # Save one annotation
#         Annotation.objects.create(
#             image=image,
#             image_label=data.get('label', 'No Label'),
#             x=float(data.get('x', 0)),
#             y=float(data.get('y', 0)),
#             width=float(data.get('width', 0)),
#             height=float(data.get('height', 0))
#         )
#         return JsonResponse({'status': 'success', 'message': 'Annotation added successfully to the database !'})
#     return JsonResponse({'status': 'failed', 'message': 'Invalid request'}, status=400)
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from annotation_backend.models import AnnotationProject, AnnotationImage, Annotation
import json

# Home page to display all projects
def index(request):
    projects = AnnotationProject.objects.all()
    selected_project = None
    images = []
    annotated_images = []

    if 'project' in request.GET and request.GET['project']:
        selected_project = get_object_or_404(AnnotationProject, id=request.GET['project'])
        all_images = AnnotationImage.objects.filter(project=selected_project)

        # Get the IDs of images already annotated in the current session
        annotated_images = request.session.get('annotated_images', [])

        # Filter images to exclude the ones already annotated in this session
        images = all_images.exclude(id__in=annotated_images)

    return render(request, 'index.html', {
        'projects': projects,
        'selected_project': selected_project,
        'images': images,
        'annotated_images': annotated_images,
    })


# Save Annotations for an Image and move to the next
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

        # Add this image to the list of annotated images in the session
        annotated_images = request.session.get('annotated_images', [])
        if image.id not in annotated_images:
            annotated_images.append(image.id)
            request.session['annotated_images'] = annotated_images

        return JsonResponse({
            'status': 'success',
            'message': 'Annotation added successfully to the database!',
            'next_image_id': get_next_image_id(image.project.id, annotated_images),
        })
    return JsonResponse({'status': 'failed', 'message': 'Invalid request'}, status=400)


# Utility to get the next image ID
def get_next_image_id(project_id, annotated_images):
    next_image = AnnotationImage.objects.filter(
        project_id=project_id
    ).exclude(id__in=annotated_images).first()
    return next_image.id if next_image else None
