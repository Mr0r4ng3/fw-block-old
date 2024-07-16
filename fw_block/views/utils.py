from django.forms import Form


def extract_errors(form: Form):

    errors = []

    for _, field in form.errors.as_data().items():

        for error in field:

            errors.append({"error": True, "reason": error.message})

    return errors
