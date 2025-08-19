import folium

mapa = folium.Map(location=[-23.55, -46.63], zoom_start=10)
folium.Marker([-23.55, -46.63], popup="São Paulo").add_to(mapa)
folium.Circle([-23.56, -46.65], radius=2000, color="red", fill=True).add_to(mapa)

mapa.save("mapa.html")
legend_html = '''
 <div style="position: fixed; 
	 bottom: 50px; left: 50px; width: 180px; height: 90px; 
	 background-color: white; z-index:9999; font-size:14px; border:2px solid grey; padding: 10px;">
	 <b>Legenda</b><br>
	 <span style="color: red; font-size:16px;">&#9679;</span> Área destacada<br>
	 <span style="color: blue; font-size:16px;">&#9679;</span> Outro exemplo<br>
	 <span style="font-size:16px;">&#9679;</span> Marcador padrão
 </div>
'''
mapa.get_root().html.add_child(folium.Element(legend_html))
mapa.save("mapa.html")
