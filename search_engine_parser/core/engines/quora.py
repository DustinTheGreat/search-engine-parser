from search_engine_parser.core.base import BaseSearch


class QuoraSearch(BaseSearch):
    """
    Searches DuckDuckGo for string
    """
    name = "Quora"
    base_url = "https://www.quora.com"
    search_url = "https://www.quora/?q={query}"
    summary = "\tQuora is a continually growing user generated collection of questions and answers.\n\t"\
        "All the questions and answers are created, edited, and organized by the people who use it."\
        " While many people use Quora as a resource for research, information, and general interest"
    def parse_soup(self, soup):
        """
        Parses DuckDuckGo Search Soup for a query results
        """
        # find all div tags
        return soup.find_all('div', class_='result')

    def parse_single_result(self, single_result):
        """
        Parses the source code to return

        :param single_result: single result found in <div id="r1-{id}">
        :type single_result: `bs4.element.ResultSet`
        :return: parsed title, link and description of single result
        :rtype: dict
        """
        h2 = single_result.find('h2', class_="result__title")
        link_tag = single_result.find('a', class_="result__url")
        desc = single_result.find(class_='result__snippet')

        # Get the text and link
        title = h2.text.strip()

        # raw link is of format "/url?q=REAL-LINK&sa=..."
        link = self.base_url + link_tag.get('href')

        desc = desc.text
        rdict = {
            "titles": title,
            "links": link,
            "descriptions": desc,
        }
        return rdict
