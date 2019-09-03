from dragonfly import routes

routes.get('articles', 'ArticleController@index')
routes.get('articles/<id:int>', 'ArticleController@show')
routes.get('articles/create', 'ArticleController@create')
routes.get('articles/<id:int>/edit', 'ArticleController@edit')

routes.post('articles', 'ArticleController@store')
routes.delete('articles/<id:int>', 'ArticleController@destroy')
routes.put('articles/<id:int>', 'ArticleController@update')
