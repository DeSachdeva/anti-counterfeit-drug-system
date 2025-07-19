
# Aushadhi Rakshak

Aushadhi Rakshak is an anti-counterfeit drug verification system that leverages synthetic DNA and cryptographic traceability to combat drug counterfeiting. The goal of this repository is to ensure the authenticity of pharmaceutical products through advanced technology integration.


## Features

- Embeds unique DNA sequences within drug packaging for physical verification.
- Prevents counterfeit drugs by ensuring tamper-proof authentication
- Builds trust among consumers, pharmacists, and regulators


## Deployed At

https://aushadhi-rakshak.vercel.app/


## Authors

- [@DeSachdeva](https://www.github.com/DeSachdeva)
- [@realSahilYadav](https://www.github.com/realSahilYadav)
- [@Anant13-spec](https://www.github.com/Anant13-Spec)


## Tech Stack

**Client:** HTML, CSS, JavaScript

**Server:** FastAPI, Python


## Run Locally

Install Python

- On Windows (winget)

```cmd
  winget install python
```
- On Mac/Linux (brew)

```cmd
   brew install python
```

Clone the project

```bash
  git clone https://github.com/DeSachdeva/anti-counterfeit-drug-system
```

Go to the project directory

```bash
  cd anti-counterfeit-drug-system
```

Go to the backend directory
```bash
  cd backend
```

Create a virtual environment

```bash
  python -m venv venv
```

Activate the virtual enivornment

- On Windows (Command Prompt)

```cmd
  venv\Scripts\activate
```

- On Mac/Linux (Terminal)

```bash
   source venv/bin/activate
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Run server

```bash
   uvicorn main:app --reload
```

Go to the frontend directory

```bash
  cd ../frontend
```
Open index.html and preview it

Access the preview at
```
  https://127.0.0.1:3000/index.html
```



## How It Works

- Manufacturers attach a QR storing medicine details and a unique hash-code on medicine package

- Consumers or Authorities verify the authenticity using a web/mobile scanner, which checks QR data against the system’s database.
## Use Cases

- Preventing fake drugs from reaching consumers
- Auditing pharmaceutical supply chain events
- Assuring regulatory compliance


## Contribution

Contributions are always welcome!

Contributions are welcome! Please fork the repository, create a new branch for your feature or bugfix, and submit a pull request.



## License

See the [LICENSE](https://github.com/DeSachdeva/anti-counterfeit-drug-system/blob/main/LICENSE) file in the repository for licensing details.

## Feedback

If you have any questions or feedback, please open an issue on the repository.


##
This README provides a high-level overview and setup guide for Aushadhi Rakshak – an anti-counterfeit drug verification system.

