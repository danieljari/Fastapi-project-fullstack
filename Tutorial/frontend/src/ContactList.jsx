import React from "react";

const ContactList = ({contacts, updateContact, updateCallback}) => {
    const onDelete = async (id) => { 
        try {
            const options = {
                method: "DELETE",
                headers: {
                    "Content-Type": "application/json"
                }
            }
            const response = await fetch(`http://127.0.0.1:5000/delete_contact/${id}`, options)
            if (response.ok) {
                updateCallback();
            } else {
                const data = await response.json();
                alert(data.message);
            }
        } catch (error) {
            console.error("Error deleting contact:", error);
        }
    }

    return <div>
         <h2> Contacts </h2>
         <table>
            <thead>
                <tr>
                    <th>First Name</th>
                    <th>Last Name</th>
                    <th>Email</th>
                    <th>Actions</th>
                </tr>
            </thead>
            <tbody>
                    {contacts.map((contact) => (
                        <tr key={contact.id}>
                            <td>{contact.firstName} </td>
                            <td>{contact.lastName} </td>
                            <td>{contact.email} </td>
                            <td>
                                 <button onClick={() => updateContact(contact)}>Update</button>
                                 <button onClick={() => onDelete(contact.id)}>Delete</button>
                            </td>
                        </tr>
                    ) )}
            </tbody>
         </table>



    </div>
}

export default ContactList