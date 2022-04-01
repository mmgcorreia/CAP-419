x_green = float(input("Passe os valores da banda espectral da faixa do verde: \n"))
x_red = float(input("Agora, passe os valores da banda espectral da faixa do vermelho: \n"))
x_nir = float(input("Por fim, passe os valores da banda espectral da faixa do infravermelho: \n"))

# NDWI
ndwi = (x_green - x_nir)/(x_green + x_nir)
print("\nNDWI:", ndwi, "\n")

# NDVI
ndvi = (x_nir - x_red)/(x_nir + x_red)
print("NDVI:", ndvi, "\n")