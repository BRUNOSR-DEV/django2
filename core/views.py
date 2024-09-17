from django.shortcuts import render

from .forms import ContatoForm, ProdutoModelForm #import da classe ContatoForm e ProdutoModelForm

from django.shortcuts import redirect 

from django.contrib import messages #import de mensagens de erro do django

from .models import Produto



# Create your views here.

#paginas html em templates
def index(request):
    context = {
        'produtos': Produto.objects.all()
    }
    return render(request, 'index.html', context)


def contato(request):
    
    form =  ContatoForm(request.POST or None) #o form pode ter dados ou não.Ele terá dados quando o usuário clicar no submit, não terá dados quando carregara página.

    if str(request.method) == 'POST': #Se o usuario submeteu o formulário - 

        if form.is_valid():     # .is_valid() retorna True se o formulário não tem erro.(obs. crsf_token precisa está válido)

            form.send_mail()

            '''nome = form.cleaned_data['nome'] # método do form - pega o valor do campo
            email = form.cleaned_data['email']
            assunto = form.cleaned_data['assunto']
            mensagem = form.cleaned_data['mensagem']

            print('Mensagem enviada! ')
            print(f' Nome: {nome} \n E-mail: {email} \n Assunto: {assunto} \n Mensagem: {mensagem}')'''

            messages.success(request, 'E-mail enviado com sucesso!')
            form = ContatoForm()
        else:
            messages.succes(request, 'Erro ao enviar e-mail')

    context = {
        'form': form
    }
    return render(request, 'contato.html', context)


def produto(request):

    #print(f'Usuário: {request.user}')

    if str(request.user) != "AnonymousUser":

        if str(request.method) == 'POST': # se o usuário enviou um POST
            form = ProdutoModelForm(request.POST, request.FILES) # request.POST = dados - request.FILES = arquivos

            if form.is_valid(): #verifica se todos os campos foram preenchidos 

                form.save()

                messages.success(request, 'Produto salvo com sucesso.')
                form = ProdutoModelForm()
            else:
                messages.error(request, 'Erro ao salvar produto.')
        else:
            form = ProdutoModelForm()

        context = {
            'form': form
        }

        return render(request, 'produto.html', context)
    else:
        return redirect('admin/login') #redirect precisa ser importado