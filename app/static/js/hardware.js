document.addEventListener("DOMContentLoaded", () => {
  const btnTema = document.getElementById("btnTema");
  const botoesFiltro = document.querySelectorAll(".filtro-btn");
  const pecas = document.querySelectorAll(".peca");
  const contadorItens = document.getElementById("contadorItens");
  const botoesExcluir = document.querySelectorAll(".btn-confirmar-exclusao");

  if (btnTema) {
    btnTema.addEventListener("click", () => {
      const claroAtivo = document.body.classList.toggle("tema-claro");
      btnTema.textContent = claroAtivo ? "Tema: Claro" : "Tema: Escuro";
    });
  }

  botoesFiltro.forEach((botao) => {
    botao.addEventListener("click", () => {
      botoesFiltro.forEach((b) => b.classList.remove("ativo"));
      botao.classList.add("ativo");

      const categoria = botao.dataset.categoria;
      let visiveis = 0;

      pecas.forEach((peca) => {
        const pertence = categoria === "todos" || peca.dataset.categoria === categoria;
        peca.style.display = pertence ? "" : "none";
        if (pertence) visiveis += 1;
      });

      if (contadorItens) {
        contadorItens.textContent = `Exibindo ${visiveis} item(ns)`;
      }
    });
  });

  botoesExcluir.forEach((botao) => {
    botao.addEventListener("click", (evento) => {
      const confirmar = window.confirm("Deseja realmente excluir este item de hardware?");
      if (!confirmar) {
        evento.preventDefault();
      }
    });
  });
});