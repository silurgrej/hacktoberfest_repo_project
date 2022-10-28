const mongoose = require('mongoose')

const userSchema = mongoose.Schema({
    email : {
        type : String,
        unique : true
    },
    password : String,
    name : String,
    dateOfBirth : Date,
    gender : String
})



var user = mongoose.model('Admins', adminsSchema);

module.exports = Admins
