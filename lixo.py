'''


<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <title>Receitas</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      background-color: #fffaf4;
      margin: 0;
      padding: 0;
    }

    .receitas-container {
      max-width: 800px;
      margin: auto;
      padding: 20px;
      text-align: center;
    }

    h2 {
      font-size: 28px;
      margin-bottom: 20px;
    }

    .titulo-receita {
      font-weight: bold;
      font-size: 20px;
      margin: 20px 0 10px;
      color: #ff7043;
    }

    .titulo-receita a {
      text-decoration: none;
      color: inherit;
    }

    .titulo-receita a:hover {
      text-decoration: underline;
    }

    .receita-foto {
      max-width: 60%;
      border-radius: 8px;
      margin-bottom: 30px;
      display: block;
      margin-left: auto;
      margin-right: auto;
    }
  </style>
</head>
<body>

  <div class="receitas-container">
    <h2>📚 Lista de Receitas</h2>
    <!-- Receita 1 -->
    <div class="titulo-receita">
      <a href="receita.html?id=50">Bolo de Milho</a>
    </div>
    <img class="receita-foto" src="imagens2/bolo-de-flocao-de-milho.jpg" alt="Bolo de Milho">

    <!-- Receita 2 -->
    <div class="titulo-receita">
      <a href="receita.html?id=10">Bife a Cavalo</a>
    </div>
    <img class="receita-foto" src="imagens2/bife_cavalo.jpg" alt="Bife a Cavalo">
  </div>

</body>
</html>





<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <title>Receitas</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      background-color: #fffaf4;
      margin: 0;
      padding: 0;
    }

    .receitas-container {
      max-width: 800px;
      margin: auto;
      padding: 20px;
      text-align: center;
    }

    h2 {
      font-size: 28px;
      margin-bottom: 20px;
    }

    .titulo-receita {
      font-weight: bold;
      font-size: 20px;
      margin: 20px 0 10px;
      cursor: pointer;
      color: #ff7043;
    }

    .titulo-receita:hover {
      text-decoration: underline;
    }

    .receita-foto {
      max-width: 60%;
      border-radius: 8px;
      margin-bottom: 30px;
      display: block;
      margin-left: auto;
      margin-right: auto;
    }
  </style>
</head>
<body>

  <div class="receitas-container">
    <h2>📚 Lista de Receitas</h2>

    <!-- Receita 1 -->
    <div class="titulo-receita" onclick="mostrarDetalhes(1)">
      Bolo de Milho
    </div>
    <img class="receita-foto" src="imagens2/bolo-de-flocao-de-milho.jpg" alt="Bolo de Milho">

    <!-- Receita 2 -->
    <div class="titulo-receita" onclick="mostrarDetalhes(2)">
      Bife a Cavalo
    </div>
    <img class="receita-foto" src="imagens2/bife_cavalo.jpg" alt="Bife a Cavalo">

    <!-- Receita 3 -->
    <div class="titulo-receita" onclick="mostrarDetalhes(3)">
      Lasanha
    </div>
    <img class="receita-foto" src="imagens2/lasanha.jpg" alt="Lasanha">

    <!-- Área para detalhes -->
    <div id="detalhes-receita"></div>
  </div>

  <script>
    const API_BASE = "https://beck-end-do-site-de-receitas-vslw.vercel.app";

    async function mostrarDetalhes(id) {
      try {
        const res = await fetch(`${API_BASE}/receita/especifico/${id}`);
        if (!res.ok) throw new Error("Erro ao buscar receita");
        const receita = await res.json();

        document.getElementById("detalhes-receita").innerHTML = `
          <h2>${receita.nome_da_receita}</h2>
          <h3>Ingredientes</h3>
          <ul>${receita.ingredientes.split("\n").map(i => `<li>${i}</li>`).join("")}</ul>
          <h3>Modo de Preparo</h3>
          <p>${receita.modo_de_preparo}</p>
        `;
      } catch (err) {
        console.error(err);
        alert("Erro ao carregar detalhes da receita");
      }
    }
  </script>

</body>
</html>








<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <title>Receitas</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      background-color: #fffaf4;
      margin: 0;
      padding: 0;
    }

    .receitas-container {
      max-width: 800px;
      margin: auto;
      padding: 20px;
      text-align: center;
    }

    h2 {
      font-size: 28px;
      margin-bottom: 20px;
    }

    .titulo-receita {
      font-weight: bold;
      font-size: 20px;
      margin: 20px 0 10px;
      color: #ff7043;
    }

    .titulo-receita a {
      text-decoration: none;
      color: inherit;
      cursor: pointer;
    }

    .titulo-receita a:hover {
      text-decoration: underline;
    }

    .receita-foto {
      max-width: 60%;
      border-radius: 8px;
      margin-bottom: 30px;
      display: block;
      margin-left: auto;
      margin-right: auto;
    }
  </style>
</head>
<body>

  <div class="receitas-container">
    <h2>📚 Lista de Receitas</h2>
    <div id="lista-receitas"></div>
  </div>

  <script>
    const API_BASE = "https://beck-end-do-site-de-receitas-vslw.vercel.app";

    // Função para buscar todas as receitas
    async function buscarReceitas() {
      const res = await fetch(`${API_BASE}/receita/receber`);
      if (!res.ok) throw new Error("Erro ao buscar receitas");
      return await res.json();
    }

    // Função para carregar receitas na lista
    async function carregarReceitas() {
      const container = document.getElementById("lista-receitas");
      container.innerHTML = "";
      const receitas = await buscarReceitas();

      receitas.forEach(r => {
        const div = document.createElement("div");
        div.innerHTML = `
          <div class="titulo-receita">
            <a href="receita.html?id=${r.id}">
              ${r.nome_da_receita}
            </a>
          </div>
          ${r.imagem_url ? `<img class="receita-foto" src="${r.imagem_url}" alt="${r.nome_da_receita}" />` : ""}
        `;
        container.appendChild(div);
      });
    }

    // Chamada inicial para carregar lista
    carregarReceitas();
  </script>

</body>
</html>






'''