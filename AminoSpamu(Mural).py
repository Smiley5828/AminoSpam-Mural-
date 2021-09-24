import AminoLab
import pyfiglet
from colorama import init, Fore, Back, Style
init()
print(Fore.RED)
print("""Script desenvolvida por: TMN SMILEY
Github : https://github.com/Smiley5828""")
print(pyfiglet.figlet_format("MURAL-SPAM", font="stop"))
client = AminoLab.Client()
email = input("Email >> ")
password = input("Senha >> ")
client.auth(email=email, password=password)
comment = input("Commentario >> ")
user_info = client.get_from_link(input("Link de Usario >> "))
user_id = user_info.object_Id; ndc_Id = user_info.ndc_Id

while True:
	try:
		client.submit_comment(ndc_Id=ndc_Id, message=comment, user_Id=user_id)
		print("Enviando comentario")
	except Exception as e:	print(e)