from flask_restful import abort

def get_model_or_404(model_class, model_id):
    instance = model_class.query.get(model_id)
    if not instance:
        message = '{} {} not found.'.format(model_class.__name__, model_id)
        abort(404, message=message)

    return instance
