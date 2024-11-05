from django.core.exceptions import ValidationError

def validate_image_size(value):
    max_size_kb = 5000  # Set maximum size (5 MB in this example)
    if value.size > max_size_kb * 1024:
        raise ValidationError(
            f"Image file size should not exceed {max_size_kb} KB.")
