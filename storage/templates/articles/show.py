def get_html(kwargs):
    template = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>''' + str(kwargs['article'].name) + '''</title>
    <link rel="stylesheet" href="https://bootswatch.com/4/materia/bootstrap.min.css">
</head>
<body>
    <div class="container">
        <br>
        <div class="card">
            <h3 class="card-header">''' + str(kwargs['article'].name) + '''</h3>
            <div class="card-body">
                <h4 class="card-text">''' + str(kwargs['article'].text) + '''</h4>
            </div>
        </div>
        <br>
        <a class="btn btn-warning" href="''' + str(kwargs['article'].url()) + '''/edit">
            Edit
        </a>
    </div>
</body>
</html>    '''
    return template