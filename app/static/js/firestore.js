document.addEventListener("DOMContentLoaded", () => {
  const btnTema = document.getElementById("btnTema");
  const botoesFiltro = document.querySelectorAll(".filtro-btn");
  const cards = document.querySelectorAll(".card");
  const contadorItens = document.getElementById("contadorItens");

  if (btnTema) {
    btnTema.addEventListener("click", () => {
      document.body.classList.toggle("tema-claro");
    });
  }

  botoesFiltro.forEach((botao) => {
    botao.addEventListener("click", () => {
      botoesFiltro.forEach((b) => b.classList.remove("ativo"));
      botao.classList.add("ativo");

      const categoria = botao.dataset.categoria;
      let visiveis = 0;

      cards.forEach((card) => {
        const pertence = categoria === "todos" || card.dataset.categoria === categoria;
        card.style.display = pertence ? "" : "none";
        if (pertence) visiveis += 1;
      });

      if (contadorItens) {
        contadorItens.textContent = `Exibindo ${visiveis} produto(s)`;
      }
    });
  });
});