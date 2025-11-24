from django.http import HttpResponse

def hola_mundo(request):
    """
    Una vista simple que retorna un saludo en HTML.
    """
    html_content = """
    <div style='font-family: sans-serif; text-align: center; padding-top: 50px;'>
        <h1>¡Hola, Bienvenido al Sistema del Equipo de I'M CLEAN!</h1>
        <p>Esta es mi primera app Django desplegada en PythonAnywhere con Github.</p>
        <p>¡Funcionó!</p>
    </div>
    """
    return HttpResponse(html_content)