def get_html(kwargs):
    template = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Edit</title>
    <link rel="stylesheet" href="https://bootswatch.com/4/materia/bootstrap.min.css">
</head>
<body>
    <div class="container">
        <br>
        <div class="card">
            <h3 class="card-header">Edit - ''' + str(kwargs['article'].name) + '''</h3>
            <div class="card-body">
                <form method="POST" action="''' + str(kwargs['article'].url()) + '''">
                    <div class="form-group">
                        <label for="name">Name:</label>
                        <input class="form-control" type="text" name="name" value="''' + str(kwargs['article'].name) + '''">
                    </div>
                    <div class="form-group">
                        <label for="text">Text:</label>
                        <input class="form-control" type="text" name="text" value="''' + str(kwargs['article'].text) + '''">
                    </div>
                    <input name="_method" type="hidden" value="PUT">

                    <button type="submit" class="btn btn-warning">Submit</button>
                </form>
                <br>
                <form method="POST" action="''' + str(kwargs['article'].url()) + '''">
                    <input name="_method" type="hidden" value="DELETE">
                    <button type="submit" class="btn btn-danger">Delete</button>
                </form>
            </div>
        </div>
        <br>
    </div>

</body>
</html>    '''
    return template