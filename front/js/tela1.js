$(document).ready(function () {
    function verDados() {
        $.ajax('http://127.0.0.1:8000/pessoas', {
            contentType: 'application/json',
            crossDomain: true,
            //data: { id: 'test', command: 'echo hello' },
            method: 'GET',
            success: function (data) {
                const tbody = $('#table-funcionarios tbody');
                tbody.empty();
                console.log(data)
                data.forEach(item => {
                    const row = $('<tr></tr>');
                    const nome = $('<td></td>').text(splitName(item.nome));
                    const data_admissao = $('<td></td>').text(formatDate(item.data_admissao));
                    const id_user = item.id;
                    const botao = $('<td></td>').html(
                        '<button onclick="verRegistro(' + id_user + ')" id="btn-ver">Ver mais</button>' +
                        ' <button onclick="editarRegistro(' + id_user + ')" id="btn-editar">Editar</button>' +
                        ' <button onclick="excluirRegistro(' + id_user + ')" id="btn-excluir">Excluir</button>' 
                    );
                    row.append(nome);
                    row.append(data_admissao);
                    row.append(botao);
                    tbody.append(row);
                });
            },
            error: function (error) {
                console.error(error);
            }
        });
    }

    verDados();
});


const splitName = (name = '') => {
    const firstName = name.split(' ').filter(Boolean);
    return firstName[0]
  }

const formatDate = (date = '') =>{
    const fDate = date.split('-').filter(Boolean);
    const year = fDate[0];
    const  month = fDate[1];
    const  day = fDate[2];
    if (day === undefined  || month === undefined  || year === undefined ) {
        return ""
    } else {
        return day + "/" + month + "/" + year;
    }
}

const verRegistro = (id = '') =>{
    window.location.href = `../pages/tela2.html?id=${id}`;
}

const novoRegistro = () =>{
    window.location.href = `../pages/tela4.html`;
}

const editarRegistro = (id = '') =>{
    window.location.href = `../pages/tela3.html?id=${id}`;
}

function excluirRegistro(id) {
    console.log("AQUI" + id)
    if (id !== undefined && id !== '') {
        $.ajax({
            url: 'http://127.0.0.1:8000/pessoas?id=' + id,
            type: 'DELETE',
            success: function (response) {
                console.log("Usuário excluído com sucesso.");
                window.alert("Usuário excluído com sucesso.");

                setTimeout(function() {
                    window.location.href = '../pages/tela1.html';
                }, 2000);
            },
            error: function (error) {
                console.error(error);
            }
        });
    } else {
        console.log("ID do usuário vazio ou não definido.");
    }
}