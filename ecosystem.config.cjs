//pm2 ecosystem config 설정파일
module.exports = {
    apps: [{
    name: 'server',
    script: './server.js',
    instances: 0,
    exec_mode: 'cluster'
    }]
  }