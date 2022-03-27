def extract_info(web_list):
    result = []

    for web in web_list:
        title = web.find("dt").find("a").string
        name = web.find("dd", {"class":"desc"}).find("a").text
        rating = web.find("div", {"class":"rating_type"}).find("strong").text
        

        web_info = {
            'title': title,
            'name': name,
            'rating': rating
        }

        result.append(web_info)

    return result
