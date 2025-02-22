import re

def markdown_to_html(markdown):
    # Títulos
    markdown = re.sub(r'^# (.+)$', r'<h1>\1</h1>', markdown, flags=re.M)
    markdown = re.sub(r'^## (.+)$', r'<h2>\1</h2>', markdown, flags=re.M)
    markdown = re.sub(r'^### (.+)$', r'<h3>\1</h3>', markdown, flags=re.M)
    # Negrito
    markdown = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', markdown)
    # Itálico
    markdown = re.sub(r'\*(.*?)\*', r'<i>\1</i>', markdown)
    # Listas ordenadas
    markdown = re.sub(r'(?<=\n)(\d+\.) (.+?)(?=\n\n|\n\s*\d+\.)', r'<li>\2</li>', markdown)
    markdown = re.sub(r'(\n<li>.+?</li>)+', r'\n<ol>\g<0>\n</ol>', markdown)
    # Links
    markdown = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', markdown)
    # Imagens
    markdown_text = re.sub(r'!\[([^\]]+)\]\(([^)]+)\)', r'<img src="\2" alt="\1"/>', markdown)
    return markdown

def create_html_file(filename, content):
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f'Arquivo HTML "{filename}" criado com sucesso.')
    except Exception as e:
        print(f'Ocorreu um erro ao criar o arquivo HTML: {e}')
        
def main():
    markdown_file = 'md/exemplo.md'
    try:
        with open(markdown_file, 'r', encoding='utf-8') as file:
            markdown_content = file.read()
            html_text = markdown_to_html(markdown_content)
            create_html_file('html/exemplo.html', html_text)
    except Exception as e:
        print(f'Ocorreu um erro ao ler o arquivo Markdown: {e}')
        
if __name__ == "__main__":
    main()