$(document).ready(function () {
    const url = window.location.href;
    const urlParams = new URL(url);
    const id_user = urlParams.searchParams.get('id');
    function verDados() {
        $.ajax('http://127.0.0.1:8000/pessoas?id'+id_user, {
            contentType: 'application/json',
            crossDomain: true,
            method: 'GET',
            success: function (data) {
                const tbody = $('#table-pessoa tbody');
                tbody.empty();
                //console.log(data)
                const row = $('<tr></tr>');
                const nome = $('<td></td>').text(splitName(data[0].nome));
                const rg = $('<td></td>').text(data[0].rg);
                const cpf = $('<td></td>').text(data[0].cpf);
                const data_nascimento = $('<td></td>').text(formatDate(data[0].data_nascimento));
                const data_admissao = $('<td></td>').text(formatDate(data[0].data_admissao));
                const botao = $('<td></td>').html(
                    ' <button onclick="editarRegistro(' + id_user + ')" id="btn-editar">Editar</button>' +
                    ' <button onclick="excluirRegistro(' + id_user + ')" id="btn-excluir">Excluir</button>'
                );
                row.append(nome);
                row.append(rg);
                row.append(cpf);
                row.append(data_nascimento);
                row.append(data_admissao);
                row.append(botao);
                tbody.append(row);
            },
            error: function (error) {
                console.error(error);
            }
        });
    }

    verDados();
});