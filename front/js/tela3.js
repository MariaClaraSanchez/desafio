$(document).ready(function () {
    const url = window.location.href;
    const urlParams = new URL(url);
    const id_user = urlParams.searchParams.get('id');

    console.log(id_user)
    function verDados() {
        $.ajax('http://127.0.0.1:8000/pessoas?id='+id_user, {
            contentType: 'application/json',
            crossDomain: true,
            method: 'GET',
            success: function (data) {
                console.log(data)
                document.getElementById("nome").value = data[0].nome;
                document.getElementById("cpf").value = data[0].cpf;
                document.getElementById("rg").value = data[0].rg;
                document.getElementById("data_nascimento").value = data[0].data_nascimento;
                document.getElementById("data_admissao").value = data[0].data_admissao;
            },
            error: function (error) {
                console.error(error);
            }
        });
    }

    verDados();

    function atualizarDados() {
        const dadosAtualizados = {
            nome: document.getElementById("nome").value,
            cpf: document.getElementById("cpf").value,
            rg: document.getElementById("rg").value,
            data_nascimento: document.getElementById("data_nascimento").value,
            data_admissao: document.getElementById("data_admissao").value,
        };

        $.ajax('http://127.0.0.1:8000/pessoas?id='+id_user, {
            contentType: 'application/json',
            crossDomain: true,
            method: 'PUT',
            data: JSON.stringify(dadosAtualizados),
            
            success: function (response) {
                console.log(response)
                window.alert("Dados atualizados com sucesso.")
            },
            error: function (error) {
                console.error(error);
            }
        });
    }

    $("#btn-update").click(function() {
        $(this).prop("disabled", true);
    
        atualizarDados();
        setTimeout(function() {
            $("#btn-update").prop("disabled", false);
        }, 5000);
    });
});