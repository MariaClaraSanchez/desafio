$(document).ready(function () {
    
    function criarDados() {
        const dadosCriar = {
            nome: document.getElementById("nome").value,
            cpf: document.getElementById("cpf").value,
            rg: document.getElementById("rg").value,
            data_nascimento: document.getElementById("data_nascimento").value,
            data_admissao: document.getElementById("data_admissao").value,
        };

        $.ajax('http://127.0.0.1:8000/pessoas', {
            contentType: 'application/json',
            crossDomain: true,
            method: 'POST',
            data: JSON.stringify(dadosCriar),
            
            success: function (response) {
                console.log(response)
                window.alert("Dados criado com sucesso.")
            },
            error: function (error) {
                console.error(error);
            }
        });
    }

    $("#btn-criar").click(function() {
        $(this).prop("disabled", true);
    
        criarDados();
        setTimeout(function() {
            $("#btn-criar").prop("disabled", false);
            window.location.href = `../pages/tela1.html`;
        }, 5000);
    });
});