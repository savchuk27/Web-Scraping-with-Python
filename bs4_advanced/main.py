from bs4 import BeautifulSoup
import re




def get_copywriter(tag):
    whois = tag.find('div', id ='whois').text.strip()
    if 'Copywriter' in whois:
        return tag
    return None


def get_salary(s):
    pattern = r'\d{1,9}'
    # salary = re.findall(pattern,s)[0]
    salary = re.search(pattern,s).group()
    print(salary)


def main():
    file = open('index.html').read()
    soup = BeautifulSoup(file,'lxml')
    # row = soup.find('div', class_ = 'row')
    # alena = soup.find('div', text='Alena').find_parent(class_='row')
    # print(alena)
    # copywriterts = []
    # persons= soup.find_all('div',class_ = 'row')
    # print(persons)

    # for person in persons:
    #     cw = get_copywriter(person)
    #     if cw:
    #         copywriterts.append(cw)
    # print(copywriterts)

    salary = soup.find_all('div', {'data-set': 'salary'})
    for i in salary:
        get_salary(i.text)






if __name__ == '__main__':
    main()