<template>
  <div>
    
    <!-- 표 -->
    <table class="table table-hover">
      <thead>
        <tr>
          <th scope="col">번호</th>
          <th scope="col">공시제출일</th>
          <th scope="col">금융회사명</th>
          <th scope="col">상품명</th>
          <th scope="col">6개월</th>
          <th scope="col">12개월</th>
          <th scope="col">24개월</th>
          <th scope="col">36개월</th>
        </tr>
      </thead>
      <tbody>
        <tr 
          v-for="(prd, index) in recommendStore.reco1D"
          :key="index"
          data-bs-toggle="modal" data-bs-target="#depositModal"
          @click="modal_click(prd)"
        >
          <th scope="row">{{ index + 1 }}</th>
          <td>{{ prd.dcls_month }}</td>
          <td>{{ prd.kor_co_nm }}</td>
          <td>{{ prd.fin_prdt_nm }}</td>
          <td>{{ getInterestRate(prd, '6') }}</td>
          <td>{{ getInterestRate(prd, '12') }}</td>
          <td>{{ getInterestRate(prd, '24') }}</td>
          <td>{{ getInterestRate(prd, '36') }}</td>
        </tr>
      </tbody>
    </table>


    <!-- 모달 -->
    <div v-if="deposit" class="modal fade deposit" id="depositModal" tabindex="-1" aria-labelledby="depositModalLabel" aria-hidden="true"  @show="drawChart">
      <div class="modal-dialog modal-dialog-scrollable modal-lg">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="depositModalLabel">{{deposit.fin_prdt_nm}}</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <table class="table table-hover">
              <tbody>
                <tr>
                  <th class="modal_row" scope="row">공시제출일</th>
                  <td>{{ deposit.dcls_month }}</td>
                </tr>
                <tr>
                  <th scope="row">금융회사명</th>
                  <td>{{ deposit.kor_co_nm }}</td>
                </tr>
                <tr>
                  <th scope="row">가입방법</th>
                  <td>{{ deposit.join_way }}</td>
                </tr>
                <tr>
                  <th scope="row">가입대상</th>
                  <td>{{ deposit.join_member }}</td>
                </tr>
                <tr>
                  <th scope="row">최고 한도</th>
                  <td>{{ deposit.max_limit }}</td>
                </tr>
                <tr>
                  <th scope="row">만기 후 이자율</th>
                  <td>{{ deposit.mtrt_int }}</td>
                </tr>
                <tr>
                  <th scope="row">우대조건</th>
                  <td>{{ deposit.spcl_cnd }}</td>
                </tr>
                <tr>
                  <th scope="row">기타 유의사항</th>
                  <td>{{ deposit.etc_note }}</td>
                </tr>
                <tr>
                  <!-- 차트 -->
                  <td v-if="deposit" colspan="7">
                    <Bar class="chart-page" :data="chartData" :options="options"/>
                  </td>                  
                </tr>
              </tbody>
            </table>


          </div>

          <!-- 가입신청 / 관심상품 저장 버튼 -->
          <div v-if="authStore.isAuthenticated" class="modal-footer no-border">
            <button type="button" class="btn btn-danger" v-if="isContracted" @click="delContract(deposit.fin_prdt_cd)">
              가입 취소
            </button>
            <button type="button" class="btn btn-primary" v-else @click="addContract(deposit)">
              가입 신청
            </button>

            <button type="button" class="btn btn-danger" v-if="isSaved" @click="delSave(deposit.fin_prdt_cd)">
              저장 취소
            </button>
            <button type="button" class="btn btn-primary" v-else @click="addSave(deposit)">
              관심상품 저장
            </button>
          </div>
          
        </div>
      </div>
    </div>

  </div>
  
</template>

<script setup>
import { useRecommendStore } from '@/stores/recommend.js'
import { useDepositStore } from '@/stores/deposit.js'
import { useAuthStore } from '@/stores/auth.js'
import { ref, computed, onMounted } from 'vue'
import axios from 'axios'
import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  BarElement,
  CategoryScale,
  LinearScale
} from 'chart.js'
import { Bar } from 'vue-chartjs'

ChartJS.register(CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend)


const depositStore = useDepositStore()
const authStore = useAuthStore()
const recommendStore = useRecommendStore()


// 기간별로 저축금리 가져오기
const getInterestRate = (prd, term) => {
  if (!prd || !prd.depositoption_set) return '-';

  const option = prd.depositoption_set.find(option => option.save_trm === term);
  return option ? option.intr_rate : '-';
}

// 기간별로 최고 우대금리 가져오기
const getInterestRate2 = (prd, term) => {
  if (!prd || !prd.depositoption_set) return '-';

  const option = prd.depositoption_set.find(option => option.save_trm === term);
  return option ? option.intr_rate2 : '-';
}


// 모달
const deposit = ref({})

const modal_click = function(prd) {
  deposit.value = prd

  // 모달창 열리면 차트 안에 데이터 갱신
  chartData.value = {
    labels: ['6개월', '12개월', '24개월', '36개월'],
    datasets: [
      {
        label: '저축 금리',
        backgroundColor: '#f87979',
        data: [
          parseFloat(getInterestRate(deposit.value, '6')) || 0,
          parseFloat(getInterestRate(deposit.value, '12')) || 0,
          parseFloat(getInterestRate(deposit.value, '24')) || 0,
          parseFloat(getInterestRate(deposit.value, '36')) || 0
        ]
      },
      {
        label: '최고 우대 금리',
        backgroundColor: '#aad1e6',
        data: [
          parseFloat(getInterestRate2(deposit.value, '6')) || 0,
          parseFloat(getInterestRate2(deposit.value, '12')) || 0,
          parseFloat(getInterestRate2(deposit.value, '24')) || 0,
          parseFloat(getInterestRate2(deposit.value, '36')) || 0
        ]
      }
    ]
  }
}


// 차트 초기설정
const chartData = ref({
      labels: [
        '6개월',
        '12개월',
        '24개월',
        '36개월',
      ],
      datasets: [
        {
          label: '저축 금리',
          backgroundColor: '#f87979',
          data: [0,0,0,0]
        },
        {
          label: '최고 우대 금리',
          backgroundColor: '#aad1e6',
          data: [0,0,0,0]
        },
      ]
    });

    // 차트 옵션 설정
    const options = {
      responsive: true,
      maintainAspectRatio: true, // 세로 길이를 고정
      aspectRatio: 2, // 세로길이 2로 설정함, 가로는 부모에 따라 조정됨
    }


// 가입한 상품 조회
const getContract = function(fin_prdt_cd) {
    axios({
      method: 'get',
      url: `${depositStore.API_URL}/fin_products/deposit_contract/${deposit.value.fin_prdt_cd}/`,
      headers: {
        Authorization: `Token ${authStore.token}`
      }
    })
      .then(response => {
        depositStore.contractedDeposit = response.data
      })
      .catch(error => {
        console.log(error)
      })
  }
onMounted(() => {
  const depositStore = useDepositStore()
  const authStore = useAuthStore()
  if (authStore.isAuthenticated && depositStore.contractedDeposit.length !== 0 && deposit.value.fin_prdt_cd) {
    getContract()
  }
})


// 상품이 계약됐는지 판단
const isContracted = computed(() => {
  if (depositStore.contractedDeposit.length === 0) {
    return false
  } 
  const findPrd = depositStore.contractedDeposit.findIndex((prd) => prd.fin_prdt_cd === deposit.value.fin_prdt_cd)
  if (findPrd !== -1) {
    return true
  }
  return false
})


// 상품 계약
const addContract = (prd) => {
  depositStore.contractedDeposit.push(prd)

  axios({
      method: 'post',
      url: `${depositStore.API_URL}/fin_products/deposit/contract/${deposit.value.fin_prdt_cd}/`,
      data: {
        fin_prdt_cd: deposit.value.fin_prdt_cd
      },
      headers: {
        Authorization: `Token ${authStore.token}`
      }
    })
      .then(response => {
      })
      .catch(error => {
        console.log(error)
      })

  }
  

// 상품 계약 취소
const delContract = (fin_prdt_cd) => {
  const idx = depositStore.contractedDeposit.findIndex((prd) => prd.fin_prdt_cd === fin_prdt_cd)
  if (idx !== -1) {

    axios({
      method: 'post',
      url: `${depositStore.API_URL}/fin_products/deposit/contract/${deposit.value.fin_prdt_cd}/`,
      data: {
        fin_prdt_cd: deposit.value.fin_prdt_cd
      },
      headers: {
        Authorization: `Token ${authStore.token}`
      }
    })
      .then(response => {
        depositStore.contractedDeposit.splice(idx, 1) 
      })
      .catch(error => {
        console.log(error)
      })
  }
}



// 관심상품 조회
const getSave = function(fin_prdt_cd) {
    axios({
      method: 'get',
      url: `${depositStore.API_URL}/fin_products/deposit/like/${deposit.value.fin_prdt_cd}/`,
      headers: {
        Authorization: `Token ${authStore.token}`
      }
    })
      .then(response => {
        depositStore.savedDeposit = response.data
      })
      .catch(error => {
        console.log(error)
      })
  }
onMounted(() => {
  const depositStore = useDepositStore()
  const authStore = useAuthStore()
  if (authStore.isAuthenticated && depositStore.savedDeposit.length !== 0 && deposit.value.fin_prdt_cd) {
    getSave()
  }
})


// 관심상품 저장하고 있는지 판단
const isSaved = computed(() => {
  console.log(depositStore.savedDeposit.length)
  if (depositStore.savedDeposit.length === 0) {
    return false
  } 
  const findPrd = depositStore.savedDeposit.findIndex((prd) => prd.fin_prdt_cd === deposit.value.fin_prdt_cd)
  if (findPrd !== -1) {
    return true
  }
  return false
})


// 관심상품 저장
const addSave = (prd) => {
  // depositStore.savedDeposit.push(prd)

  axios({
      method: 'post',
      url: `${depositStore.API_URL}/fin_products/deposit/like/${deposit.value.fin_prdt_cd}/`,
      data: {
        fin_prdt_cd: deposit.value.fin_prdt_cd
      },
      headers: {
        Authorization: `Token ${authStore.token}`
      }
    })
      .then(response => {
        depositStore.savedDeposit.push(prd)
        console.log(depositStore.savedDeposit)
      })
      .catch(error => {
        console.log(error)
      })

  }
  

// 관심상품 저장 취소
const delSave = (fin_prdt_cd) => {
  const idx = depositStore.savedDeposit.findIndex((prd) => prd.fin_prdt_cd === fin_prdt_cd)
  if (idx !== -1) {

    axios({
      method: 'post',
      url: `${depositStore.API_URL}/fin_products/deposit/like/${deposit.value.fin_prdt_cd}/`,
      data: {
        fin_prdt_cd: deposit.value.fin_prdt_cd
      },
      headers: {
        Authorization: `Token ${authStore.token}`
      }
    })
      .then(response => {
        depositStore.savedDeposit.splice(idx, 1) 
      })
      .catch(error => {
        console.log(error)
      })
  }
}
</script>


<style scoped>
.modal_row {
  width: 150px;
}
.no-border {
  border: none;
}
/* .chart-page {
  width: 100%;
  height: 30px;
} */
</style>
