from django.shortcuts import render, redirect
from .separate_folium import *
from django.http import HttpResponse
from .models import MapDatabase


def home_page(request):
	return render(request, "testmap/home.html")


# test
def pls_news(request):
	return render(request, "testmap/pls-news.html")
def pls_news_map(request):
	return render(request, "testmap/pls-news-map.html")












# pls news page code
def dynamic_map(request):
    """dynamic_map() takes a database object (map's html in string format) and renders it in a normal html file
    returns html file with created map """
    httpstring = MapDatabase.objects.get(id=1)
    vaule_of_httpstring = httpstring.html_string
    return HttpResponse(vaule_of_httpstring)

def map_create(request):
	'''map creating automation needs to be done'''
	created_mymap = None

	created_mymap = create_map(created_mymap, 15.9613,206.3672,2)

	add_news(created_mymap, 36.4033,127.8618,
                                    '일회용 수저 빼달랬는데 왜 자꾸 주나요',
                                    'https://lh3.googleusercontent.com/HJ_dm8aHGoGcaZuWmmpRWJ5bF64Q2X5uC6ijjCaRxkkEGUDhblHd7rymVsZHF96w233KHyULvHN43aiX_A-fTd30Hh_38pkCNPbWqeWkyfcaG2Sh89yKWfdnYJojDoZeJkRHN87TLfA=w2400',
                                    'http://www.segye.com/newsView/20191004509710?OutUrl=Zum')
	add_news(created_mymap,  60.9241, 246.0938,
                                    '녹차 티백 한 개에 미세 플라스틱 100억개?',
                                    'https://lh3.googleusercontent.com/8LRbI58r6_UAYdyZUpncuC5dcA6LSk1l3y9nSyqC9FE1yTA4x36-jnCcaCiLuNHdHcZ0Q83CMkZiQ5djfjWD2DC2BJudAaD1jdzBW2NYi0ZKpe4Yc6bNvFcHAzVQHu2bBd5TPiHOuS8=w2400',
									'http://www.realfoods.co.kr/view.php?ud=20191004000707')

	add_news(created_mymap,  7.6313, 125.1664,
	                                    '고래뱃속 쓰레기, 유산된 새끼 발견"플라스틱이 영양분 흡수 방해"',
	                                    'https://upload.wikimedia.org/wikipedia/commons/6/6a/Eubalaena_glacialis_with_calf.jpg',
										 'http://www.ccreview.co.kr/news/articleView.html?idxno=208173')
	add_news(created_mymap,   49.8380,  262.2656,
	                                    '플라스틱 안된다고 가시 돋친 나무스푼 주면',
	                                    'https://lh3.googleusercontent.com/8DDwNg5A6pJvHrSbAV74Cd5HCvQbYWKnp7KJ2SA8VZYv4hBajKZeXRw2xuL0LrZDyjABHTdXnf-Z9XH3ARVEvNpKhfcsWbPJEwYh1d3qFfaDYFfXTlF0GpXTLa9NwKzHkwBSfImdvvk=w2400',
										'https://www.yna.co.kr/view/AKR20190927146700505?input=1195m')
	add_news(created_mymap,   35.7465, 258.7500,
	                                    '환경걱정 NO...먹을 수 있는 식용 빨대 나온다',
	                                    'https://lh3.googleusercontent.com/lFK9xdR4Wz3tXVmIDrxFgGUZL04srvFq_hMHrvB0uWnFFZGeA5Z7LJnnc37YiLs1n97xTn-iyp1uB9Tc-g4L0RnstqVYGhTMOTdqaxVg2MjWuptWy9-MqtOIIals-cnIRY4wCMjZwzk=w2400',
										 'http://www.jejusori.net/news/articleView.html?idxno=307500')
	add_news(created_mymap,   33.3929,126.5400,
	                                    '플라스틱 섬 제주 살릴 Green 아이디어',
	                                    'https://lh3.googleusercontent.com/PN0ENmGEqqlP9S0Lfj841eNwmh9pxqBMwg6C2cYfSIz5DAKZQ1hQUlDGPurKwad4Lu-8kck7xvyw6ZEipbKMG3GUWZcTGw4iwvKT81ZcrmyxYBw66QWg_eZXpHlv4JaXlkt5waqxMZk=w2400',
										'http://www.maeilnews.co.kr/news/article.html?no=5188')
	add_news(created_mymap,   42.5193, 12.8002,
                                    	'In Rome, you can swap 30 plastic bottles for a subway ride',
	                                    'https://lh3.googleusercontent.com/FrJ2vwbKxK22hwBhApiQqULAgHoeeaLO3P_3adNWaw2jx_NaImkFwCuUSjpZ-zOcmOapyV9XwmWEefQQ-eUYj7w1ZefWwUdWj2qZS5fZRCxuCNqzzkXFKr3mqhGDAdHzzDAkj2vI--Q=w2400',
										'https://www.fastcompany.com/90386534/in-rome-you-can-swap-30-plastic-bottles-for-a-subway-ride')
	add_news(created_mymap, 36.0591, 139.2808,
                                    '일본은 폐플라스틱 처리 후진국',
                                    'https://lh3.googleusercontent.com/aNCup04x8CJvrKRFgzTMCU7oY72-A43_SLB8IwOZI_JBVW1Dpkwb3KL_6_eBmwHTlXJdU89fidnJriLuIkvkFSel47EYa4egC6p3uZ5U6MPlQ-qHpP7J0lT2YhDcQeGW5AlxO8zV-vI=w2400',
                                    'http://www.pressm.kr/news/articleView.html?idxno=25369')





	# gyres
	custom_img_marker(created_mymap, 34.0162, -45.0000, 'north atlantic gyre', 'static/whirlpool.png')
	custom_img_marker(created_mymap, -41.7713, -13.7109, 'south atlantic gyre', 'static/whirlpool.png')
	custom_img_marker(created_mymap, -27.3718, 82.9688, 'indian gyre', 'static/whirlpool.png')
	custom_img_marker(created_mymap, 31.3536, -157.1484, 'north pacific gyre', 'static/whirlpool.png')
	custom_img_marker(created_mymap, -39.0960, -132.5391, 'south pacific gyre', 'static/whirlpool.png')
	custom_img_marker(created_mymap, 39.6395, 194.0625, 'north pacific gyre', 'static/whirlpool.png')
	custom_img_marker(created_mymap, -40.1789, 238.7109, 'south pacific gyre', 'static/whirlpool.png')

	resolution, width, height = 75, 7, 3
	iframe_img(created_mymap, resolution, width, height,
           "https://upload.wikimedia.org/wikipedia/commons/f/f4/Mercator_projection_SW.jpg",
           34.0162, -45.0000)

	#north pacific gyre / gpgp
	iframe_img_para(created_mymap, resolution, width, height,
           'https://media.nationalgeographic.org/assets/photos/cc2/bba/cc2bbae1-0699-45b9-b86e-a03a23b28077.jpg',
           39.6395, 194.0625,
		   'The Great Pacific Garbage Patch is a collection of marine debris in the North Pacific Ocean. \
		   Marine debris is litter that ends up in oceans, seas, and other large bodies of water. \
		   The Great Pacific Garbage Patch, aka. the Pacific trash vortex, \
		   spans waters From the West Coast of North America to Japan.')
	iframe_img_para(created_mymap, resolution, width, height,
           'https://media.nationalgeographic.org/assets/photos/315/1e1/3151e1d5-0177-4238-bcc9-8ffd67f15e42.jpg',
           39.6395, 200,
		   'Ocean gyres are large system of circular ocean currents formed by global wind patterns and forces created by Earths rotation. \
		   The five major circulation patterns formed by the currents on this map are the worlds five major ocean gyres: North Atlantic, \
		   South Atlantic, Indian, North Pacific, and South Pacific.')
	iframe_img_para(created_mymap, resolution, width, height,
           'https://media.nationalgeographic.org/assets/photos/315/1e1/3151e1d5-0177-4238-bcc9-8ffd67f15e42.jpg',
           42.6395, 200,
		   'Ocean plastic can persist in sea surface waters, eventually accumulating in remote areas of the world’s oceans. \
		   Here we characterise and quantify a major ocean plastic accumulation zone formed in subtropical waters between \
		   California and Hawaii: The Great Pacific Garbage Patch (GPGP). Our model, calibrated with data from multi-vessel and aircraft \
		   surveys, predicted at least 79 (45–129) thousand tonnes of ocean plastic are floating inside an area of 1.6 million km2; a figure \
		   four to sixteen times higher than previously reported. ')




	#created_mymap.save('templates/testmap/created_mymap.html')
	maps_as_string = created_mymap.get_root().render()

	my_map_object = MapDatabase(id=1, html_string=maps_as_string)
	my_map_object.save()
	return redirect('created_map')


def created_map(request):
    return render(request, "testmap/plastic_news.html")












# pls islands page code
def dynamic_map2(request):
    """dynamic_map() takes a database object (map's html in string format) and renders it in a normal html file
    returns html file with created map """
    httpstring = MapDatabase.objects.get(id=2)
    vaule_of_httpstring = httpstring.html_string
    return HttpResponse(vaule_of_httpstring)

def map_create2(request):
	'''map creating automation needs to be done'''
	created_mymap = None
	created_mymap = create_map(created_mymap, 15.9613,206.3672,2)


	custom_img_marker(created_mymap, 34.0162, -45.0000, 'north atlantic gyre', 'static/whirlpool.png')
	custom_img_marker(created_mymap, -41.7713, -13.7109, 'south atlantic gyre', 'static/whirlpool.png')
	custom_img_marker(created_mymap, -27.3718, 82.9688, 'indian gyre', 'static/whirlpool.png')
	custom_img_marker(created_mymap, 31.3536, -157.1484, 'north pacific gyre', 'static/whirlpool.png')
	custom_img_marker(created_mymap, -39.0960, -132.5391, 'south pacific gyre', 'static/whirlpool.png')
	custom_img_marker(created_mymap, 39.6395, 194.0625, 'north pacific gyre', 'static/whirlpool.png')
	custom_img_marker(created_mymap, -40.1789, 238.7109, 'south pacific gyre', 'static/whirlpool.png')


	country_df = pd.read_csv('country.csv',  na_values = False)

	# Plastic waste generation per person, 2010
	csv_df = pd.read_csv('plastic-waste-per-capita.csv', na_values = False)
	waste_df = pd.merge(csv_df, country_df, how='outer')
	waste_df = waste_df.fillna(0)
	waste_df['Year'] = waste_df['Year'].astype('int')
	waste_df['Numeric code'] = waste_df['Numeric code'].astype('int')

	for i in range(0, len(waste_df)):
	    folium.Circle(
	    location = [waste_df.iloc[i]['Latitude'], waste_df.iloc[i]['Longitude']],
	    popup = waste_df.iloc[i]['Entity'],
	    radius = waste_df.iloc[i]['Per capita plastic waste (kilograms per person per day)'] * 1000 * 500,
	    color = 'orange',
	    fill = True,
	    fill_color = 'orange'
	    ).add_to(created_mymap)


	# 2010 gdp per capita
	csv_df2 = pd.read_csv('gdp-per-capita-worldbank.csv', na_values = False)
	csv_df2 = csv_df2.set_index(['Year'])
	csv_df2 = csv_df2.loc[2010]

	gdp_df = pd.merge(csv_df2, country_df, how='outer')
	gdp_df = gdp_df.fillna(0)

	for i in range(0, len(gdp_df)):
	    folium.Circle(
	    location = [gdp_df.iloc[i]['Latitude'], gdp_df.iloc[i]['Longitude']],
	    popup = gdp_df.iloc[i]['Entity'],
	    radius = gdp_df.iloc[i]['GDP per capita (int.-$) (constant 2011 international $)'] *5,
	    color = 'lightgray',
	    fill = True,
	    fill_color = 'lightgray'
	    ).add_to(created_mymap)





	#created_mymap.save('templates/testmap/created_mymap.html')
	maps_as_string = created_mymap.get_root().render()

	my_map_object = MapDatabase(id=2, html_string=maps_as_string)
	my_map_object.save()
	return redirect('created_map2')


def created_map2(request):
    return render(request, "testmap/gdp_waste.html")
















# pls data visualization1 page code
def dynamic_map3(request):
    """dynamic_map() takes a database object (map's html in string format) and renders it in a normal html file
    returns html file with created map """
    httpstring = MapDatabase.objects.get(id=3)
    vaule_of_httpstring = httpstring.html_string
    return HttpResponse(vaule_of_httpstring)

def map_create3(request):
	'''map creating automation needs to be done'''
	created_mymap = None
	created_mymap = create_map(created_mymap, 15.9613,206.3672,2)


	custom_img_marker(created_mymap, 34.0162, -45.0000, 'north atlantic gyre', 'static/whirlpool.png')
	custom_img_marker(created_mymap, -41.7713, -13.7109, 'south atlantic gyre', 'static/whirlpool.png')
	custom_img_marker(created_mymap, -27.3718, 82.9688, 'indian gyre', 'static/whirlpool.png')
	custom_img_marker(created_mymap, 31.3536, -157.1484, 'north pacific gyre', 'static/whirlpool.png')
	custom_img_marker(created_mymap, -39.0960, -132.5391, 'south pacific gyre', 'static/whirlpool.png')
	custom_img_marker(created_mymap, 39.6395, 194.0625, 'north pacific gyre', 'static/whirlpool.png')
	custom_img_marker(created_mymap, -40.1789, 238.7109, 'south pacific gyre', 'static/whirlpool.png')






	country_df = pd.read_csv('country.csv',  na_values = False)
	# Share of plastic waste that is inadequately managed, 2010
	csv_df = pd.read_csv('inadequately-managed-plastic.csv', na_values = False)
	mismanaged_df = pd.merge(csv_df, country_df, how='outer')
	#mismanaged_df.head()
	mismanaged_df = mismanaged_df.fillna(0)
	#mismanaged_df.head()

	for i in range(0, len(mismanaged_df)):
	    folium.Circle(
	        location = [mismanaged_df.iloc[i]['Latitude'], mismanaged_df.iloc[i]['Longitude']],
	        popup = mismanaged_df.iloc[i]['Entity'],
	        radius = mismanaged_df.iloc[i]['Share of plastic inadequately managed (%)'] * 4000,
	        color = 'yellow',
	        fill = True,
	        fill_color = 'yellow'
	    ).add_to(created_mymap)

	#2010 Total plastic waste by country
	csv_df2 = pd.read_csv('plastic-waste-generation-total.csv', na_values = False)
	waste_df = pd.merge(csv_df2, country_df, how='outer')
	#waste_df.head()
	waste_df = waste_df.fillna(0)

	for i in range(0, len(waste_df)):
	    folium.Circle(
	        location = [waste_df.iloc[i]['Latitude'], waste_df.iloc[i]['Longitude']],
	        popup = waste_df.iloc[i]['Entity'],
	        radius = waste_df.iloc[i]['Plastic waste generation (tonnes, total) (tonnes per year)'] / 40,
	        color = 'crimson',
	        fill = True,
	        fill_color = 'red'
	    ).add_to(created_mymap)















	#created_mymap.save('templates/testmap/created_mymap.html')
	maps_as_string = created_mymap.get_root().render()

	my_map_object = MapDatabase(id=3, html_string=maps_as_string)
	my_map_object.save()
	return redirect('created_map3')


def created_map3(request):
    return render(request, "testmap/plastic_data.html")
