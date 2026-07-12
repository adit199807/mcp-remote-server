import asyncio
from mcp.server.fastmcp import FastMCP


mcp = FastMCP('shah-mcp-trial')

@mcp.tool()
def greetUser(userName:str)->str:
    """
    Please use this to greet a user
    args:
        userName: is the user name of the given user to be greeted
    """
    return f'HI {userName}, nice to meet you'

def main():
    print('starting server')
    asyncio.run(mcp.run(transport='streamable-http'))


if __name__ == '__main__':
    asyncio.run(mcp.run(transport='streamable-http'))
