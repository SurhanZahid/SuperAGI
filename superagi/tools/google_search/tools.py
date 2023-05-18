#-------------------------------------Calling AbstractTools Function-------------------------------------#
"""Utility for the Google search API."""

from typing import Optional
from superagi.tools.abstract_tool import AbstractTool
from superagi.helper.google_search import GoogleSearchAPIWrap


class SearchGoogleAPI(AbstractTool):
    """A tool to query the Google search API."""

    name = "Google Search"
    description = (
        "An interface for Google Search. "
        "Helpful for answering questions about current events. "
        "The input should be a search query."
        "The output is a string of the query results"
    )
    api_wrapper: GoogleSearchAPIWrap

    def _exec(
        self,
        query: str,
    ) -> str:
        """Execute the tool."""
        return self.api_wrapper.exec(query)


class RetrieveGoogleSearchResults(AbstractTool):
    """A tool to query the Google Search API and obtain JSON results."""

    name = "Google Search Results JSON"
    description = (
        "An interface for Google Search. "
        "Helpful for answering questions about current events. "
        "The input should be a search query. The output is a JSON array of the query results"
        "The number of results to return can be specified."
    )
    num_results: int = 3
    api_wrapper: GoogleSearchAPIWrap

    def _exec(
        self,
        query: str,
    ) -> str:
        """Execute the tool."""
        return str(self.api_wrapper.retrieve_result(query, self.num_results))