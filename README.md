# Taggy
Tag based resources server


## Data security
While https can protect your data from unwanted eyes during transfer between the server and your computer, anyone with access to the database can read your deepest secrets.

As **Taggy** can be used both hosted or installed on a company server, you want to avoid that these secrets can be read by the database administrator.
As a single shared encryption key would be useless, data is encrypted using a user specific encryption key.
 
But because **Taggy** is a system where resources are meant to be shared between multiple persons, secrets entered by one user, need to be accessible by others (while you don't know their password). To get around this, asymmetric encryption is used and shared, encrypted resources are encrypted using the public key of everyone that needs access.

When accessing an encrypted resource, it is decrypted using your own private key. This private key is saved in the database in encrypted form using a symmetric encryption algorithm. 
Upon loading of the **Taggy** application, your encrypted private key is downloaded to your local machine. When it's required, you will be prompted for your encryption password 
(different from your account password) and the private key is decrypted locally, and then used to decrypt the secret you wanted to access.

The private key will stay unencrypted in your local machine's memory for a configurable amount of time, or until you manually lock it again.

- The private key is never unencrypted on the server
- The password you use to encrypt your private key is never sent to the server
- It is not possible to reset this password if you forget it (we can't recover your private key without it)
- Secrets shared with other users can be made available again after generating a new private-public key pair, but requires the intervention of another user
- Encrypted data is not indexed for the search function, as such, it's not possible to use search for the content of encrypted data