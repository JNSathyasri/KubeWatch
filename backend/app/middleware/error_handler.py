from flask import jsonify


def register_error_handlers(app):

    @app.errorhandler(404)
    def not_found(error):
        return (
            jsonify(
                {
                    "success": False,
                    "error": "Endpoint not found",
                }
            ),
            404,
        )

    @app.errorhandler(500)
    def server_error(error):
        app.logger.exception(error)

        return (
            jsonify(
                {
                    "success": False,
                    "error": "Internal Server Error",
                }
            ),
            500,
        )