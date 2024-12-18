import os
import django
from django.conf import settings
from annotation_backend.models import AnnotationProject, AnnotationImage
from django.core.files import File


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project.settings')  # 
django.setup()

def populate_annotation_project():

    project_name = "project_1"
    project_description = "This is the first annotation project."

    # Create or get the AnnotationProject object
    project, created = AnnotationProject.objects.get_or_create(name=project_name, description=project_description)
    if created:
        print(f'AnnotationProject "{project_name}" created.')
    else:
        print(f'AnnotationProject "{project_name}" already exists.')

    # Step 2: Get all images from the images folder
    image_folder = os.path.join(settings.BASE_DIR, 'images')  # Assuming 'images' folder is at the base directory
    if not os.path.exists(image_folder):
        print(f"Image folder '{image_folder}' does not exist.")
        return

    image_files = [f for f in os.listdir(image_folder) if f.endswith(('.jpg', '.jpeg', '.png'))]
    if not image_files:
        print(f"No images found in '{image_folder}' folder.")
        return

    # Step 3: Upload images and create AnnotationImage
    for image_file in image_files:
        image_path = os.path.join(image_folder, image_file)
        with open(image_path, 'rb') as img_file:
            annotation_image = AnnotationImage(project=project)
            annotation_image.image.save(image_file, File(img_file), save=True)
            annotation_image.save()
            print(f'AnnotationImage for "{image_file}" created successfully.')

    print('All images uploaded and linked to AnnotationProject.')

if __name__ == "__main__":
    populate_annotation_project()
