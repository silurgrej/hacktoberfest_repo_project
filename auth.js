const user = require('../../../../../models/user/user')

const {OAuth2Client} = require('google-auth-library')
const jwt = require('jsonwebtoken');
require('dotenv').config();


const client = new OAuth2Client("499316289094-jrcm8c2ugt7d7hobasv2sh2u63a7d1r1.apps.googleusercontent.com")

const googlelogin = (req,res) => {
  const {tokenId} = req.body
  client.verifyIdToken({idToken:tokenId,audience : "499316289094-jrcm8c2ugt7d7hobasv2sh2u63a7d1r1.apps.googleusercontent.com"}).then(response=>{
    const {email_verified,name,email} = response.payload;
    if(email_verified)
    {
        user.findOne({email:email}).exec((err,admin)=>{
            if(err){
                return res.status(400).json({error:"Something went wrong"})
            }
            else{
                if(admin){
                    const token = jwt.sign({emailID:user.email,type:'user'},process.env.JWT_KEY,{expiresIn:'7d'});
                    res.json({token,user:{emailID : user.email,type:'user'}})
                }
                else{
                    return res.status(400).json({error:"Something went wrong"})
                }
            }
        })
    }
  })
}

module.exports = { googlelogin}
