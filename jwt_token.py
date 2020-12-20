#this is Generate_key by jwt
import jwt
from Config import config
def Generate_key():
    token=None
    try:
        jwt_token = jwt.encode({'exp':datetime.utcnow()+timedelta(minutes=1440)},key=Config.SECRET_KEY)
        return jwt_token

    except Exception as err:
        return jsonify(err)
""" componentDidMount()
{
  let url:"http://127.0.0.1:5000/api/upload";
  fetch(url,{method:'POST',headers:{'x-access-token':'6961d7333843f1a7c280ffda57c5f3',
  'Content-type':'application/json'}}).then((result)=>{
    result.json().then((resp)=>{
    this.setState({data:resp})
    })
  })
      }

    onChange(e)
      {
        let files=e.target.files;
        console.warn(files);
        let reader =new global.FilerReader();
        reader.readAsDataURL(files[1])
        reader.onload=(e)=>{
            console.warn(e.target.result);
        let url="http://127.0.0.1:5000/api/upload";
        fetch(url,{method:'POST',headers:{'x-access-token':'6961d7333843f1a7c280ffda57c5f3',
          'Content-type':'application/json'}}).then((result)=>{
            result.json().then((resp)=>{
            this.setState({data:resp})
            })
          })
        }

      }
      render(){
        const data=this.state.data
        console.warn(data);
        return(
          <div onSubmit={this.onFormSubmit}>
          <input type="file" name="file" onChange={(e)=>this.onChange(e)}/>
          </div>
        );
      }
}"""
