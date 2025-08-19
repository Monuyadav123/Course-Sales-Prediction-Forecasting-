def estimate_staff_required(predicted_sales, ratio=50):
    """Estimate number of staff required. Default: 1 staff per 50 enrollments."""
    staff_needed = int(predicted_sales / ratio)
    return staff_needed
