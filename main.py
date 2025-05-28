<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Contador de Silêncio - Gestão do Condomínio</title>
  <style>
    body {
      background-color: #0d1117;
      color: #f0f0f0;
      font-family: Arial, sans-serif;
      margin: 0;
      padding: 20px;
      text-align: center;
    }
    h1 {
      color: #d90429;
      font-size: 2.4em;
    }
    .contador {
      font-size: 2em;
      font-weight: bold;
      color: red;
      margin: 30px 0;
    }
    .botao {
      padding: 10px 20px;
      font-size: 18px;
      border: none;
      border-radius: 5px;
      margin: 10px;
      cursor: pointer;
    }
    .whatsapp {
      background-color: #25D366;
      color: white;
    }
    .email {
      background-color: #d00000;
      color: white;
    }
    .alerta {
      background-color: #003566;
      padding: 15px;
      border-radius: 8px;
      margin-top: 30px;
      font-size: 16px;
    }
    blockquote {
      font-style: italic;
      margin-top: 30px;
      font-size: 18px;
    }
    .rodape {
      font-size: 14px;
      margin-top: 10px;
    }
  </style>
</head>
<body>
  <h1>📢 Contador de Silênçio da Gestão do Condomínio</h1>
  <p>Desde o dia <strong>23 de maio de 2025, às 12h</strong>, aguardamos uma resposta da gestão (síndico e conselho fiscal).</p>
  <p>Tempo decorrido:</p>
  <div class="contador" id="contador"></div>

  <a href="https://wa.me/?text=Veja%20o%20contador%20de%20sil%C3%AAncio:%20https://silencio.streamlit.app" target="_blank">
    <button class="botao whatsapp">📲 Compartilhar no WhatsApp</button>
  </a>
  <a href="mailto:sindico@exemplo.com?subject=Omiss%C3%A3o%20de%20resposta&body=Prezados,%0A%0AO%20sil%C3%AAncio%20da%20gest%C3%A3o%20condominial%20persiste%20desde%2023/05/2025%20%C3%A0s%2012h.%0AConfira%20o%20contador%20em%20tempo%20real:%20https://silencio.streamlit.app%0A%0AAtenciosamente,%0ACond%C3%B4mino%20vigilante" target="_blank">
    <button class="botao email">🚨 Denunciar por E-mail</button>
  </a>

  <div class="alerta">⚖️ O Código Civil (art. 1.348, VIII) exige que o síndico preste contas e responda aos condôminos. Omissão pode configurar infração legal.</div>
  <blockquote>“Transparência não é favor. É dever.”</blockquote>
  <p class="rodape">Aplicativo criado por condôminos vigilantes para promover transparência e boa gestão.</p>

  <script>
    const inicio = new Date('2025-05-23T12:00:00');
    function atualizarContador() {
      const agora = new Date();
      const diff = agora - inicio;
      const dias = Math.floor(diff / (1000 * 60 * 60 * 24));
      const horas = Math.floor((diff / (1000 * 60 * 60)) % 24);
      const minutos = Math.floor((diff / (1000 * 60)) % 60);
      const segundos = Math.floor((diff / 1000) % 60);
      document.getElementById('contador').innerText = `${dias} dias, ${horas}h ${minutos}min ${segundos}s de silênçio`;
    }
    setInterval(atualizarContador, 1000);
    atualizarContador();
  </script>
</body>
</html>
