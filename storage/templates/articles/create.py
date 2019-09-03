def get_html(kwargs):
    template = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Create</title>
    <link rel="stylesheet" href="https://bootswatch.com/4/materia/bootstrap.min.css">
</head>
<body>
    <div class="container">
        <br>
        <div class="card">
            <h3 class="card-header">Create</h3>
            <div class="card-body">
                <form method="POST" action="http://localhost:8080/articles">
                    <div class="form-group">
                        <label for="name">Name:</label>
                        <input class="form-control" type="text" name="name">
                    </div>
                    <div class="form-group">
                        <label for="text">Text:</label>
                        <input class="form-control" type="text" name="text">
                    </div>
                    <button type="submit" class="btn btn-warning">Submit</button>
                </form>
            </div>
        </div>
        <br>
    </div>
</body>
</html>    '''
    return template