export const api = {
  resHandle(res,target,failType){
		return new Promise((resolve,reject)=>{
			let statusF=res.data.ret==1
			if (failType) {
				target.$message({
				  message: res.data.message,
				  type: statusF?'success':failType
				});
			}
			if (statusF) {
				resolve(statusF);
			}else{
				reject(statusF);
			}
		})
	},
  getImg(data) {
    return axios({
      url: "/plus",
      method: "post",
      data: data
    })
	},
	getPerentArea(data){
		// console.log(data)
		 return axios({
			url:"/areas/",
			method:"get",
			data:data
		 })	
	},
	getSubsArea(data){
		// console.log(data)
		 return axios({
			url:"/areas/" + data.id,
			method:"get",
			data:data
		 })	
	},
	getPersonInfo(data){
		// console.log(data)
		 return axios({
			url:"/persons/" + data.id,
			method:"get",
			data:data
		 })	
	},
}