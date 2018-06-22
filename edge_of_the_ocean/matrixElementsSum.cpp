int matrixElementsSum(std::vector<std::vector<int>> matrix) {
    int row_size = matrix.size(); /* size of y */
    int column_size = matrix[0].size();
    int total_elements = row_size + column_size;
    std::cout<<"row: "<<row_size<<" column: "<<column_size<<std::endl;
    std::vector<int> one_d_vector;
    for(int i = 0;i < row_size; i++){
        for(int j = 0; j < column_size; j++)
        {
            one_d_vector.push_back(matrix[i][j]);
        }
    }
    std::cout<<one_d_vector.size()<<std::endl;
    int accumulator = 0;
    for(int i = 0; i < column_size; i++){
        for(int j = 0; j < total_elements; j+=column_size){
            if(one_d_vector[i+j] > 0)
            {
                accumulator+=one_d_vector[i+j];
                std::cout<<one_d_vector[i+j]<<" i:"<<i<<" j: "<<j<<std::endl;
                if(j != 0){
                    int k = column_size;
                    accumulator+=one_d_vector[i+j+k];
                    std::cout<<one_d_vector[i+j+k]<<" i:"<<i<<" j: "<<j<<" k: "<<k<<std::endl;
                }
            }
            else{
                std::cout<<one_d_vector[i+j]<<" i:"<<i<<" j: "<<j<<std::endl;
                break;
            }

        }
    }

    return accumulator;
}
