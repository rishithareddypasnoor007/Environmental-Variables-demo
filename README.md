Dotenv

Dotenv is a zero-dependency module that loads environment variables from a .env file into process.env. Storing configuration in the environment separate from code is based on The Twelve-Factor App methodology.

Process.env  ->   returns an object containing the user environment. 

The Twelve-Factor App - The twelve-factor app stores config in environment variables (often shortened to env vars or env). Env vars are easy to change between deploys without changing any code; unlike config files, there is little chance of them being checked into the code repo accidentally.

Place all the required variables into  .env 

Not to track them by git you can place the .env  in  .gitignore


Include:

from dotenv import load_dotenv
load_dotenv()



At this point, parsed key/value from the .env file is now present as system environment variable and they can be conveniently accessed via os.getenv():


