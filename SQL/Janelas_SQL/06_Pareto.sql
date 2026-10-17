-- Percentuais acumulados para análise de Pareto

-- Moostrar o percentual acumulado em relação ao total (ex: regra do Pareto - 80/20)
-- Exemplo prático: Identificar quais produtos contribuem mais para o faturamento
SELECT 
    nome_produto, 
    total_receita,
    SUM(total_receita) OVER (ORDER BY total_receita DESC) /
    SUM(total_receita) OVER () * 100 AS percentual_acumulado
FROM (
    SELECT
        produtos.id_produto,
        produtos.nome_produto,
        SUM(vendas.receita_venda) AS total_receita
    FROM produtos
    LEFT JOIN vendas ON produtos.id_produto = vendas.id_produto
    GROUP BY produtos.id_produto, produtos.nome_produto
) AS tabela;