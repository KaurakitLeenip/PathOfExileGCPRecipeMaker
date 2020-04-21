def emit_message(message, app):
    app.emit('newstatus', {'line': message}, namespace='/')