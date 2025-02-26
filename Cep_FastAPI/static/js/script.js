        document.getElementById('cep-form').addEventListener('submit', function(event) {
            event.preventDefault();
            const cep = document.getElementById('cep').value;
            fetch(`/consultar_cep/${cep}/`)
                .then(response => response.json())
                .then(data => {
                    const resultadoDiv = document.getElementById('resultado');
                    if (data.erro) {
                        resultadoDiv.innerHTML = `<p>CEP não encontrado.</p>`;
                    } else {
                        resultadoDiv.innerHTML = `
                            <p><strong>Endereço:</strong></p>
                            <p>${data.logradouro}, ${data.bairro}, ${data.localidade} - ${data.uf}</p>
                        `;
                    }
                })
                .catch(error => {
                    document.getElementById('resultado').innerHTML = `<p>Ocorreu um erro. Tente novamente.</p>`;
                });
        });