# Bu proje, NewsApi.org üzerinden Wall Street makalelerini alarak veriyi çekme, güncelleme, silme ve ekleme işlemlerini gerçekleştiren bir sistemdir.


from requests import get
from pprint import pprint
from uuid import uuid4

# region Task 1
# NewsApi.org üzerinden Wall Street makalelerini alarak veriyi bir sözlük (dictionary) olarak döndürelim.
def get_data() -> dict:
    return get('https://newsapi.org/v2/everything?domains=wsj.com&apiKey=47f3419f49864ca889f632677d485de1').json()

# endregion



# region Task 2
# Her bir makaleye, id anahtarına uuid4() fonksiyonu kullanılarak benzersiz bir UUID atayın. Bu UUID'ler, her makaleyi tanımlamak için kullanılacaktır.
def assigned_id(data: dict) -> dict:
    for article in data.get('articles'):
        article['_id'] = str(uuid4())

    return data
# endregion



# region Task 3
# Kullanıcıdan yazar ismini alalım ve bu yazarın yazdığı makaleleri ekrana basarak gösterelim.
def get_article_by_author_name(data: dict, author_name: str) -> dict:
    for article in data['articles']:
        if article['author'] == author_name:
            return article

    return {
        'Notification': 'There is no such article!'
    }


# endregion



#region task 4
# "Title" göre ekrana basalım ancak makalenin başlığı içinde geçip geçmediğini kontrol edilerek ekrana basma işlemi gerçekleştirelim.
def get_article_by_title(data: dict, title: str) -> dict:
    for article in data['articles']:
        if article['title'].__contains__(title):
            return article

    return {
        'Notification': 'There is no such article!'
    }


#endregion



# region Task 5
# Makaleden, yazar bilgisi (author) None olanları silmek
def remove_article(data: dict) -> dict:
    for article in data['articles']:
        if article['author'] is None:
            data['articles'].remove(article)

    return data

#endregion



# region task 6
# Id Silme İşlemi.
def delete_article(data: dict, _id: str) -> dict:
    for article in data['articles']:
        if article['_id'] == _id:
            data['articles'].remove(article)

    return data


#endregion



# region Task 7
# Yaratma İşlemi
def create(author: str,
           content: str,
           desctiption: str,
           published_at: str,
           id_source: str,
           name_source: str,
           title: str,
           url: str,
           url_to_image: str,
           data: dict):
    data['articles'].append(
        {
            '_id': str(uuid4()),
            'author': author,
            'content': content,
            'desctiption': desctiption,
            'published_at': published_at,
            'source': {
                'id': id_source,
                'name': name_source
            },
            'title': title,
            'url': url,
            'urlToImage': url_to_image
        }
    )

    print('Article has been created!')
#endregion



# region Task 8
# Güncelleme İşlemi

def update(_id: str,
           author: str,
           content: str,
           desctiption: str,
           published_at: str,
           id_source: str,
           name_source: str,
           title: str,
           url: str,
           url_to_image: str,
           data: dict):


    for article in data['articles']:
        if article['_id'] == _id:
            article.update(
                {
                    'author': author,
                    'content': content,
                    'desctiption': desctiption,
                    'published_at': published_at,
                    'source': {
                        'id': id_source,
                        'name': name_source
                    },
                    'title': title,
                    'url': url,
                    'urlToImage': url_to_image
                }
            )

    print('Article has been edited!')
# endregion




def main():
    data = get_data()

    clean_data = remove_article(data)

    my_data = assigned_id(clean_data)

    while True:
        process = input('Type a process : ')

        match process:
            case 'get data':
                pprint(my_data)
            case 'get by author name':
                article = get_article_by_author_name(
                    my_data,
                    input('Author Name : ')
                )

                pprint(article)
            case 'get by title':
                article = get_article_by_title(
                    my_data,
                    input('Title: ')
                )

                pprint(article)
            case 'create':
                create(
                    input('Author : '),
                    input('Content : '),
                    input('Description : '),
                    input('Published Date : '),
                    input('Source Id : '),
                    input('Source Name : '),
                    input('Title : '),
                    input('Url : '),
                    input('Image : '),
                    my_data
                )
                print(my_data)
            case 'update':
                update(
                    input('Id : '),
                    input('Author : '),
                    input('Content : '),
                    input('Description :'),
                    input('Published Date : '),
                    input('Source Id : '),
                    input('Source Name : '),
                    input('Title : '),
                    input('Url : '),
                    input('Image: '),
                    my_data
                )
                print(my_data)
            case 'delete':
                data = delete_article(
                    my_data,
                    input('Id : ')
                )
                pprint(data)
            case _:
                print('Please type valid process!')


main()
