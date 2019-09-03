def get_html(kwargs):
    template = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Index</title>
    <link rel="stylesheet" href="https://bootswatch.com/4/materia/bootstrap.min.css">
</head>
<body>
    <div class="container">
        <br>
        <div class="card">
            <div class="card-body">
                <h4 class="card-title">Articles</h4>
                <div class="list-group list-group-flush">'''
    for article in kwargs['articles']:
        template += '''                    <a href="''' + str(article.url()) + '''" class="list-group-item list-group-item-action flex-column align-items-start">
                        <div class="d-flex w-100 justify-content-between">
                            <h5 class="mb-1">''' + str(article.name) + '''</h5>
                        </div>
                        <p class="mb-1">''' + str(article.text) + '''</p>
                    </a>

'''
    template += '''
                </div>
            </div>
        </div>
        <br>
         <a class="btn btn-success" href="http://localhost:8080/articles/create">
            Create
        </a>
    </div>
</body>
</html>    '''
    return template