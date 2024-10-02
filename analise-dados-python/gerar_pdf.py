from fpdf import FPDF # type: ignore

# Criar o PDF com os gráficos salvos
pdf = FPDF()

# Definindo as dimensões da página
largura = 210  # Largura da página A4 em mm
altura = 297   # Altura da página A4 em mm

# Adicionando a página de capa
pdf.add_page()
pdf.set_font('Arial', 'B', 24)
pdf.set_xy(0, altura / 2 - 30)  # Colocando o título no meio verticalmente
pdf.cell(0, 40, 'Análise de Dados da Educação no Brasil', 0, 1, 'C')

pdf.set_font('Arial', 'B', 16)
pdf.cell(0, 10, 'Desigualdade nos Cursos de Especialização por Estado', 0, 1, 'C')

pdf.set_font('Arial', '', 12)
pdf.cell(0, 10, 'Relatório gerado por Mariana Gomes', 0, 1, 'C')
pdf.cell(0, 10, 'Data: 25 de Setembro de 2024', 0, 1, 'C')

# Adicionar página inicial
pdf.add_page()

# Definir fonte e título principal
pdf.set_font('Arial', 'B', 16)
pdf.cell(200, 10, txt="Análise de Dados - Cursos de Especialização", ln=True, align='C')

# Adicionando uma breve descrição
pdf.set_font('Arial', '', 12)
pdf.ln(10)
pdf.multi_cell(0, 10, txt="A desigualdade na educação é um desafio persistente no Brasil, afetando o acesso e a qualidade do ensino em diferentes regiões do país. As disparidades entre estados e municípios impactam diretamente as oportunidades dos estudantes, especialmente no ensino superior. Este relatório apresenta uma análise dos dados dos cursos de especialização oferecidos no Brasil em 2022, com foco na distribuição de vagas, instituições e modalidades de ensino, evidenciando as desigualdades regionais e oferecendo insights para uma melhor compreensão do cenário educacional atual.")

# Adicionando uma breve descrição
pdf.set_font('Arial', 'B', 12)
pdf.ln(10)
pdf.multi_cell(0, 10, txt="Segue abaixo alguns gráficos para melhor entendimento da análise desta situação:")

# Gráfico 1: Top 10 Cursos mais Frequentes
pdf.add_page()
pdf.set_font('Arial', 'B', 14)
pdf.cell(200, 10, txt="Top 10 Cursos de Especialização mais Frequentes", ln=True, align='C')
pdf.ln(10)
pdf.image('grafico_1.png', x=10, w=190)

# Adicionando uma breve descrição
pdf.set_font('Arial', '', 12)
pdf.ln(10)
pdf.multi_cell(0, 10, txt="Este gráfico destaca os 10 cursos de especialização mais ofertados em 2022, revelando as áreas com maior demanda e popularidade no Brasil. A predominância de cursos específicos reflete as tendências de especialização profissional e as necessidades do mercado de trabalho.")

# Gráfico 2: Situação das Vagas por Estado (UF)
pdf.add_page()
pdf.set_font('Arial', 'B', 14)
pdf.cell(200, 10, txt="Situação das Vagas por Estado (UF)", ln=True, align='C')
pdf.ln(10)
pdf.image('grafico_2.png', x=10, w=190)

# Adicionando uma breve descrição
pdf.set_font('Arial', '', 12)
pdf.ln(10)
pdf.multi_cell(0, 10, txt="O gráfico acima apresenta a situação das vagas de cursos de especialização por unidade federativa, mostrando a discrepância entre os estados com maior e menor oferta. Isso ilustra as desigualdades regionais e as disparidades de acesso à educação especializada.")

# Gráfico 3: Situação Nacional
pdf.add_page()
pdf.set_font('Arial', 'B', 14)
pdf.cell(200, 10, txt="Proporção de Vagas por Situação no Brasil", ln=True, align='C')
pdf.ln(10)
pdf.image('grafico_3.png', x=10, w=190)

# Adicionando uma breve descrição
pdf.set_font('Arial', '', 12)
pdf.ln(10)
pdf.multi_cell(0, 10, txt="A distribuição das vagas de cursos de especialização por situação evidencia a relação entre vagas preenchidas, disponíveis e ociosas. Essa análise aponta para a eficiência no preenchimento das vagas ofertadas, além de revelar onde existem mais oportunidades não aproveitadas.")

# Gráfico 4: Distribuição das Modalidades de Ensino
pdf.add_page()
pdf.set_font('Arial', 'B', 14)
pdf.cell(200, 10, txt="Distribuição das Modalidades de Ensino", ln=True, align='C')
pdf.ln(10)
pdf.image('grafico_5.png', x=10, w=190)

# Adicionando uma breve descrição
pdf.set_font('Arial', '', 12)
pdf.ln(10)
pdf.multi_cell(0, 10, txt="Este gráfico mostra a proporção entre as diferentes modalidades de ensino (presencial, EAD, etc.) ofertadas nos cursos de especialização. A predominância de uma modalidade sobre a outra reflete as mudanças nas preferências de ensino e as condições regionais para implementação dessas modalidades.")

# Gráfico 5: Top 10 Municípios com Mais Cursos
pdf.add_page()
pdf.set_font('Arial', 'B', 14)
pdf.cell(200, 10, txt="Top 10 Municípios com Mais Cursos", ln=True, align='C')
pdf.ln(10)
pdf.image('grafico_6.png', x=10, w=190)

# Adicionando uma breve descrição
pdf.set_font('Arial', '', 12)
pdf.ln(10)
pdf.multi_cell(0, 10, txt="A análise dos 10 municípios que mais ofertam cursos de especialização evidencia a centralização da oferta educacional em determinados polos, reforçando a desigualdade de acesso nas regiões mais afastadas.")

# Gráfico 6: Distribuição de Cursos por Região
pdf.add_page()
pdf.set_font('Arial', 'B', 14)
pdf.cell(200, 10, txt="Distribuição de Cursos por Região", ln=True, align='C')
pdf.ln(10)
pdf.image('grafico_7.png', x=10, w=190)

# Adicionando uma breve descrição
pdf.set_font('Arial', '', 12)
pdf.ln(10)
pdf.multi_cell(0, 10, txt="Este gráfico ilustra a distribuição geográfica dos cursos de especialização no Brasil, destacando as regiões com maior concentração de ofertas. As disparidades regionais são evidentes, com maior número de cursos concentrados no Sudeste e Nordeste, enquanto outras regiões enfrentam escassez.")

# Adicionando a página de conclusão
pdf.add_page()
pdf.set_font('Arial', 'B', 16)
pdf.cell(0, 10, 'Conclusão', 0, 1, 'C')

pdf.set_font('Arial', '', 12)
pdf.multi_cell(0, 10, """
A análise dos dados de cursos de especialização no Brasil revela uma significativa 
desigualdade educacional entre os estados. Enquanto estados do Sudeste e Sul mostram
uma maior oferta de cursos e vagas, as regiões Norte e centro-oeste enfrentam uma escassez
preocupante. Esse cenário reflete a histórica falta de investimento em educação nas
regiões menos desenvolvidas, o que compromete o acesso à educação de qualidade e o
desenvolvimento de profissionais especializados. No ultimo grafico, pode-se observar um pequeno avanço da região nordeste em comparação com as outras, mesmo ainda sendo pequeno comparando com a região sudeste, a região nordeste conseguiu estar na frente de regiões como sul e centro-oeste.

O estudo destaca a necessidade urgente de políticas públicas que promovam uma 
redistribuição mais equitativa dos recursos educacionais, a fim de proporcionar 
oportunidades de formação iguais para todos os cidadãos brasileiros, independentemente 
da sua localização geográfica.
""")

# Salvar o PDF
pdf.output("cursos_de_especializacao.pdf")