class Abertura {
    constructor(nome, lances, variantes, oph, jogadores) {
        this.nome = nome;
        this.lances = lances;
        this.variantes = variantes;
        this.oph = oph;
        this.jogadores = jogadores;
    }
}

class AberturaCadastro {
    constructor() {
        this.aberturas = []; 
        this.indiceEditando = null;
    }

    adicionarAbertura(abertura) {
        if (this.indiceEditando !== null) {
            this.aberturas[this.indiceEditando] = abertura;
            this.indiceEditando = null;
        } else {
            this.aberturas.push(abertura);
        }
        this.atualizarTabela();
    }

    removerAbertura(indice) {
        this.aberturas.splice(indice, 1);
        this.atualizarTabela();
    }

    editarAbertura(indice) {
        const abertura = this.aberturas[indice];
        document.getElementById("nome").value = abertura.nome;
        document.getElementById("lances").value = abertura.lances;
        document.getElementById("variantes").value = abertura.variantes;
        document.getElementById("oph").value = abertura.oph;
        document.getElementById("jogadores").value = abertura.jogadores;
        this.indiceEditando = indice;
    }

    atualizarTabela() {
        const tabela = document.getElementById("tabelaAberturas");
        tabela.innerHTML = "";

        for (let i = 0; i < this.aberturas.length; i++) {
            const abertura = this.aberturas[i];
            const linha = document.createElement("tr");

            linha.innerHTML = `
                <td>${abertura.nome}</td>
                <td>${abertura.lances}</td>
                <td>${abertura.variantes}</td>
                <td>${abertura.oph}</td>
                <td>${abertura.jogadores}</td>
                <td>
                    <button onclick="AberturaCadastro1.removerAbertura(${i})" class="btn btn-danger btn-sm">Excluir</button>
                    <button onclick="AberturaCadastro1.editarAbertura(${i})" class="btn btn-warning btn-sm">Editar</button>
                </td>
            `;
            tabela.appendChild(linha);
        }
    }
}

const AberturaCadastro1 = new AberturaCadastro();
const formulario = document.getElementById('aberturaForm');
formulario.addEventListener('submit', function (evento) {
    evento.preventDefault();
    const nome = document.getElementById('nome').value;
    const lances = document.getElementById('lances').value;
    const variantes = document.getElementById('variantes').value;
    const oph = document.getElementById('oph').value;
    const jogadores = document.getElementById('jogadores').value;
    const abertura = new Abertura(nome, lances, variantes, oph, jogadores);
    AberturaCadastro1.adicionarAbertura(abertura);
});

document.getElementById("botaoAtualizar").addEventListener("click", function () {
    const nome = document.getElementById('nome').value;
    const lances = document.getElementById('lances').value;
    const variantes = document.getElementById('variantes').value;
    const oph = document.getElementById('oph').value;
    const jogadores = document.getElementById('jogadores').value;
    const abertura = new Abertura(nome, lances, variantes, oph, jogadores);
    AberturaCadastro1.adicionarAbertura(abertura);
});