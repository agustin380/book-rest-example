from flask_restful import abort

def get_model_or_404(model_class, model_id):
    """Get a model instance. If it doesn't exist, abort with a 404 status code.

    :param model_class: the model class of the instance.
    :type model_class: flask_sqlalchemy.db.Model
    :param model_id: the id of the model instance.
    :type model_id: int
    :return: model instance.
    :rtype: flask_sqlalchemy.db.Model
    """
    instance = model_class.query.get(model_id)
    if not instance:
        message = '{} {} not found.'.format(model_class.__name__, model_id)
        abort(404, message=message)

    return instance
